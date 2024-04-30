import React, { useState, useEffect } from "react";
import NavbarMain from "../../components/NavbarMain/NavbarMain";
import SensorCardComponent from "../../components/Card/SensorCard";
import api from "../../api/api";
import 'virtual-select-plugin/dist/virtual-select.min.css';
import 'virtual-select-plugin/dist/virtual-select.min.js';
import './../Sensor/Sensor.css'
import CreateDevices from "./Create";
import { MDBInput } from 'mdb-react-ui-kit';

const Sensor = () => {
    const [displaySidebar, setDisplaySidebar] = useState(true);
    const [sensor, setSensor] = useState([]);
    const [displayMenu, setDisplayMenu] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");
    const [displayedSensors, setDisplayedSensors] = useState([]);

    const fetchSensor = () => {
        api.get('/api/all-sensor', {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}',
            },
        }).then(response => {
            console.log(response.data);
            setSensor(response.data);
            setDisplayedSensors(response.data); // Initialize displayed devices with all devices
        });
    };

    useEffect(() => {
        fetchSensor();
    }, []);

    const searchHandler = (event) => {
        const query = event.target.value.toLowerCase();
        setSearchQuery(query);
        const filteredSensors = sensor.filter(sensor => sensor.name.toLowerCase().includes(query));
        setDisplayedSensors(filteredSensors);
    };

    return (
        <div style={{ height: "100%" }}>
            <NavbarMain navbarVisibility={{ displaySidebar, setDisplaySidebar }} menuVisibility={{ displayMenu, setDisplayMenu }} />
            <div className="wrapper-card" style={{ marginTop: "10vh" }}>
                <CreateDevices />
                <div>
                    <MDBInput label='Search Sensor by Name' id='searchQuery' type='text' size="lg" name="searchQuery" required onChange={(e) => { searchHandler(e) }} />
                    {displayedSensors.map((sensor) => (
                        <SensorCardComponent
                            key={sensor.id}
                            name={sensor.name}
                            id={sensor.id}
                            sensorAlertValue={sensor.value}
                            sensorAlertDirection={
                                sensor.alertDirection === 1 ? "Value Less than alert value is Better" :
                                    sensor.alertDirection === 0 ? "Value Between range is Better" :
                                        sensor.alertDirection === -1 ? "Value Higher than alert value is Better" :
                                            "Invalid Alert Direction"
                            } upperRangeAlertValue={sensor.upperValueRange}
                            lowerRangeAlertValue={sensor.lowerValueRange}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Sensor;
