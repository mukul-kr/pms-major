import React, { useState, useEffect } from "react";
import NavbarMain from "../../components/NavbarMain/NavbarMain";
import CardComponent from "../../components/Card/Card";
import api from "../../api/api";
import 'virtual-select-plugin/dist/virtual-select.min.css';
import 'virtual-select-plugin/dist/virtual-select.min.js';
import './../Devices/Devices.css'
import CreateDevices from "./Create";
import { MDBBtn, MDBInput } from 'mdb-react-ui-kit';

const Devices = () => {
    const [displaySidebar, setDisplaySidebar] = useState(true);
    const [devices, setDevices] = useState([]);
    const [displayMenu, setDisplayMenu] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");
    const [displayedDevices, setDisplayedDevices] = useState([]);

    const fetchDevices = () => {
        api.get('/api/device', {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}',
            },
        }).then(response => {
            console.log(response.data);
            setDevices(response.data);
            setDisplayedDevices(response.data); // Initialize displayed devices with all devices
        });
    };

    useEffect(() => {
        fetchDevices();
    }, []);

    const searchHandler = (event) => {
        const query = event.target.value.toLowerCase();
        setSearchQuery(query);
        const filteredDevices = devices.filter(device => device.ext_id.toLowerCase().includes(query));
        setDisplayedDevices(filteredDevices);
    };

    return (
        <div style={{ height: "100%" }}>
            <NavbarMain navbarVisibility={{ displaySidebar, setDisplaySidebar }} menuVisibility={{ displayMenu, setDisplayMenu }} />
            <div className="wrapper-card" style={{ marginTop: "10vh" }}>
                <CreateDevices />
                <div>
                    <MDBInput label='Search by device name' id='s_device_name' type='text' size="lg" name="s_device_name" required onChange={(e) => { searchHandler(e) }} />
                    {displayedDevices.map((device) => (
                        <CardComponent
                            key={device.id}
                            name={device.ext_id}
                            id={device.id}
                            password={device.secret}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Devices;
