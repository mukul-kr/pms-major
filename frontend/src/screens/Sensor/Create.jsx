import React, { useState, useEffect } from "react";
import NavbarMain from "../../components/NavbarMain/NavbarMain";
import CardComponent from "../../components/Card/Card";
import api from "../../api/api";
import 'virtual-select-plugin/dist/virtual-select.min.css';
import 'virtual-select-plugin/dist/virtual-select.min.js';
import './../Devices/Devices.css'
import { useNavigate } from "react-router-dom";
import { MDBBtn, MDBInput, MDBRadio } from 'mdb-react-ui-kit';

const CreateSensors = () => {
    const [sensorName, setSensorName] = useState("");
    const [sensorAlertValue, setSensorAlertValue] = useState(0);
    const [upperRangeAlertValue, setUpperRangeAlertValue] = useState(0);
    const [lowerRangeAlertValue, setLowerRangeAlertValue] = useState(0);
    const [sensorAlertDirection, setSensorAlertDirection] = useState('1');

    const handleSensorNameChange = (event) => {
        setSensorName(event.target.value);
    }

    const handleSensorAlertValueChange = (event) => {
        setSensorAlertValue(event.target.value);
    }

    const handleSensorAlertDirectionChange = (event) => {
        setSensorAlertDirection(event.target.value);
    }

    const handleUpperRangeAlertValueChange = (event) => {
        setUpperRangeAlertValue(event.target.value);
    }

    const handleLowerRangeAlertValueChange = (event) => {
        setLowerRangeAlertValue(event.target.value);
    }

    const createSensor = () => {

        api.post('/api/sensor', {
            "sn": sensorName,
            "alertDirection": Number(sensorAlertDirection),
            "value": Number(sensorAlertValue),
            "upperValueRange": Number(upperRangeAlertValue),
            "lowerValueRange": Number(lowerRangeAlertValue)
        }).then(response => {
            console.log(response.data);
            window.location.reload();
        });

    }

    return (
        <>

            <MDBInput label='Sensor Name' id='sen_name' type='text' size="lg" name="sen_name" required onChange={(e) => { handleSensorNameChange(e) }} />


            <div style={{ display: 'grid', justifyContent: 'center', margin: '10px' }}>

                <MDBRadio label='Value Higher than alert value is Better' id='1' value="1" name="direction" defaultChecked inline onChange={(e) => { handleSensorAlertDirectionChange(e) }} />

                <MDBRadio label='Value Equal to alert value is Better' id='0' value="0" name="direction" inline onChange={(e) => { handleSensorAlertDirectionChange(e) }} />

                <MDBRadio label='Value Equal to alert value is Better' id='-1' value="-1" name="direction" inline onChange={(e) => { handleSensorAlertDirectionChange(e) }} />


            </div>

            {/* if sensorAlertDirection is not 0 then show the below one else print nothing */}
            {sensorAlertDirection !== '0' ? (
                <MDBInput label='Sensor Alert Value' id='sensorAlertValue' type='text' size="lg" name="sensorAlertValue" required onChange={(e) => { handleSensorAlertValueChange(e) }} />
            ) : (
                <>
                    <MDBInput label='Sensor Lower Alert Value' id='lowerRangeAlertValue' type='text' size="lg" name="lowerRangeAlertValue" required onChange={(e) => { handleLowerRangeAlertValueChange(e) }} />
                    <MDBInput label='Sensor Upper Alert Value' id='sensorUpperAlertValue' type='text' size="lg" name="sensorUpperAlertValue" required onChange={(e) => { handleUpperRangeAlertValueChange(e) }} />
                </>
            )}
<div style={{ display: 'grid', justifyContent: 'center', margin: '10px' }}>
            <MDBBtn onClick={createSensor}  >Create Sensor</MDBBtn>
</div>

        </>
    );
};

export default CreateSensors;
