import React from 'react';
import {Routes, Route} from 'react-router-dom';
import HomeScreen from './screens/HomeScreen';
import AuthScreen from './screens/AuthScreen/AuthScreen';
import Userprofile from './screens/Userprofile/Userprofile';
import Analytics from './screens/Analytics/Analytics';
import Devices from './screens/Devices/Devices';
import Sensor from './screens/Sensor/Sensor';

const AllRoutes = () => {
    return(
        <Routes>
            <Route path='/' element={<HomeScreen/>} />
            <Route path='/auth' element={<AuthScreen/>} />
            <Route path='/user-profile' element={<Userprofile/>}/>
            <Route path='/analytics' element={<Analytics/>}/>
            <Route path='/devices' element={<Devices/>} />
            <Route path='/sensor' element={<Sensor/>} />
        </Routes>
    )
}

export default AllRoutes