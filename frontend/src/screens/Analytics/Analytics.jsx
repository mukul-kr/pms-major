import React from "react";
import NavbarMain from "../../components/NavbarMain/NavbarMain";
import { useState, useEffect } from "react";
import api from "../../api/api";
import 'virtual-select-plugin/dist/virtual-select.min.css';
import 'virtual-select-plugin/dist/virtual-select.min.js';
import './../Analytics/Analytics.css'
import { MDBBtn, MDBInput } from "mdb-react-ui-kit";
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import moment, { min } from "moment";


const Analytics = () => {

    const [displaySidebar, setDisplaySidebar] = useState(true)
    const [displayMenu, setDisplayMenu] = useState(false)
    const [devices, setDevices] = useState()
    const [sensors, setSensors] = useState()

    const [selDevices, setSelDevices] = useState()
    const [selSensors, setSelSensors] = useState()
    const [startDate, setStartDate] = useState()
    const [endDate, setEndDate] = useState()
    const [graphDataFetched, setGraphDataFetched] = useState(false)

    const [data, setData] = useState()
    const [datasets, setDatasets] = useState([])
    const [options, setOptions] = useState({
        chart: {
            type: 'line',
            zoomType: 'x',
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Date and Time',
            },
        },
        yAxis: {
            title: {
                text: 'Data Value',
            },
        },
        title: {
            text: 'Data chart'
        },
        series: []
    })

    const fetchDevices = () => {
        api.get('/api/device', {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}',
            },
        }).then(response => {
            console.log(response.data)
            setDevices(response.data)
        })
    }

    const fetchSensors = () => {
        api.get('/api/sensor', {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}',
            },
        }).then(response => {
            console.log(response.data)
            setSensors(response.data)
        })
    }

    useEffect(() => {
        fetchDevices()
        fetchSensors()

    }, [])

    // useeffect called every 5 min
    useEffect(() => {
        const interval = setInterval(() => {
            if (graphDataFetched) {
                getGraphData();
            }
        }, 3000);
        return () => clearInterval(interval);
    }, []);

    const getGraphData = () => {
        setGraphDataFetched(true);
        console.log("clicked")
        setDatasets([])
        setData()
        const dataparam = {
            params: {
                "start_date": new Date(startDate).toISOString(),
                "end_date": new Date(endDate).toISOString(),
            }
        }

        var urlString = "/api/data" + "?start_date=" + startDate + "&end_date=" + endDate

        for (var i = 0; i < selDevices.length; i++) {
            urlString = urlString + "&device_ids=" + selDevices[i]
        }

        for (var j = 0; j < selSensors.length; j++) {
            urlString = urlString + "&sensor_ids=" + selSensors[j]
        }


        console.log(dataparam)
        var int_sensor_array = selSensors.map((item) => { return parseInt(item) })
        console.log(selDevices, int_sensor_array, new Date(startDate).toISOString(), new Date(endDate).toISOString())
        api.get(urlString
            , {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
            }).then(response => {
                console.log(response.data)
                setData(response.data)
                response.data.map(function (data_each) {
                    var sn = data_each.sensor_id
                    if (!datasets[sn]) {
                        datasets[sn] = {
                            name: sensors.find(sensor => sensor.id === sn).name,
                            data: [],
                        };
                    }
                    const date = new Date(data_each.created_at);
                    date.setMinutes(date.getMinutes() + 30)
                    date.setHours(date.getHours() + 5)
                    const localDate = date.toISOString();
                    var dateTime = moment.utc(localDate).valueOf();
                    datasets[sn].data.push([dateTime, data_each.value]);
                })
                console.log(datasets)
                setOptions({
                    chart: {
                        type: 'line',
                        zoomType: 'x',
                        height: 700
                    },
                    xAxis: {
                        type: 'datetime',
                        title: {
                            text: 'Date and Time',
                        },
                    },
                    yAxis: {
                        title: {
                            text: 'Data Value',
                        },
                    },
                    title: {
                        text: 'Data chart'
                    },
                    series: datasets
                })
            })
    }


    window.VirtualSelect.init({
        ele: '#device-dropdown',
        search: true,
        optionSelectedText: 'devices Selected',
        optionsSelectedText: 'devices Selected',
        allOptionsSelectedText: 'All decices',
        searchPlaceholderText: 'Select all',
        alwaysShowSelectedOptionsCount: true,
    });

    window.VirtualSelect.init({
        ele: '#sensors-dropdown',
        search: true,
        optionSelectedText: 'sensors Selected',
        optionsSelectedText: 'sensors Selected',
        allOptionsSelectedText: 'All sensors',
        searchPlaceholderText: 'Select all',
        alwaysShowSelectedOptionsCount: true,
    });

    if (document.querySelector('#device-dropdown')) {
        document.querySelector('#device-dropdown').addEventListener('change', function () {
            setSelDevices(this.value)
        });
    }

    if (document.querySelector('#sensors-dropdown')) {
        document.querySelector('#sensors-dropdown').addEventListener('change', function () {
            setSelSensors(this.value)
        });
    }

    return (
        <div style={{ height: "100%" }}>
            <NavbarMain navbarVisibility={{ displaySidebar, setDisplaySidebar }} menuVisibility={{ displayMenu, setDisplayMenu }} />
            <div className="wrapper-graph">
                <div className="filters">

                    <div className="drop-down-filters">
                        <div>
                            {devices != null ?
                                <select id="device-dropdown" name="devices" placeholder="Select devices" multiple data-selected="all" >
                                    {devices.map(function (device) {
                                        return (
                                            <option value={device.ext_id} key={device.id}>{device.ext_id}</option>
                                        )
                                    })}
                                </select> : <></>}
                        </div>

                        <div>
                            {sensors != null ? <select id="sensors-dropdown" name="sensors" placeholder="Select Sensors" multiple data-selected="all">
                                {sensors.map(function (sensor) {
                                    return (
                                        <option value={sensor.id} key={sensor.id}>{sensor.name}</option>
                                    )
                                })}
                            </select> : <></>}
                        </div>
                    </div>
                    <div className="date-filters">
                        <div>
                            <MDBInput
                                type="datetime-local"
                                id="start-date"
                                value={startDate}
                                onChange={(e) => { setStartDate(e.target.value) }}
                            />
                            {/* <input type="datetime-local" id="start-date" onChange={(e) => { setStartDate(e.target.value) }} /> */}
                        </div>
                        <div>
                            <MDBInput
                                type="datetime-local"
                                id="end-date"
                                value={endDate}
                                onChange={(e) => { setEndDate(e.target.value) }}
                            />
                        </div>
                    </div>
                </div>
                <center style={{ marginTop: "20px", paddingLeft: "65px", width: "calc(100% - 70px)" }}><MDBBtn onClick={getGraphData}>Submit</MDBBtn></center>

                <div className="graph-container">
                    <HighchartsReact highcharts={Highcharts} options={options} />
                </div>
            </div>
        </div>
    )
}
export default Analytics