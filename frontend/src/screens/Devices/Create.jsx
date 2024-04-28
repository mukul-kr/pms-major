import React, { useState, useEffect } from "react";
import NavbarMain from "../../components/NavbarMain/NavbarMain";
import CardComponent from "../../components/Card/Card";
import api from "../../api/api";
import 'virtual-select-plugin/dist/virtual-select.min.css';
import 'virtual-select-plugin/dist/virtual-select.min.js';
import './../Devices/Devices.css'
import { useNavigate } from "react-router-dom";
import { MDBBtn, MDBInput } from 'mdb-react-ui-kit';

const CreateDevices = () => {
    const [deviceName, setDeviceName] = useState("");
    const [deviceSecurityKey, setDeviceSecurityKey] = useState("");
    const navigate = useNavigate()

    const handleDeviceNameChange = (event) => {
        setDeviceName(event.target.value);
    }

    const handleDeviceSecurityKeyChange = (event) => {
        setDeviceSecurityKey(event.target.value);
    }

    const createDevice = () => {

        api.get("/auth/profile", {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
        }).then(response => {
            console.log(response.data)
            const user_id = response.data.id
            api.post('/api/device', {
                ext: deviceName,
                u: user_id,
                p: deviceSecurityKey,
            }).then(response => {
                console.log(response.data);
                window.location.reload();
            });
        }).catch(error => {
            // navigate('/')
            console.log(error)
        })

    }

    return (
        <>
        <div style={{ display: 'grid', justifyContent: 'center', margin: '10px' }}>
            
            <MDBInput style={{ width: '15vw', display: 'grid', justifyContent: 'center' }} label='Device Name' id='dev_name' type='text' size="lg" name="dev_name" required onChange={(e) => { handleDeviceNameChange(e) }} />
            <div style={{padding: "10px"}}></div>
            <MDBInput style={{ width: '15vw', display: 'grid', justifyContent: 'center' }} label='Security Key' id='sec_key' type='text' size="lg" name="sec_key" required onChange={(e) => { handleDeviceSecurityKeyChange(e) }} />
            <div style={{ display: 'grid', justifyContent: 'center', margin: '10px' }}>
                <MDBBtn onClick={createDevice} >Create Device</MDBBtn>
            </div>
        </div>
        </>
    );
};

export default CreateDevices;
