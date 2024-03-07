import React from 'react';
import {Routes, Route} from 'react-router-dom';
import HomeScreen from './screens/HomeScreen';
import AuthScreen from './screens/AuthScreen/AuthScreen';


const AllRoutes = () => {
    return(
        <Routes>
            <Route path='/' element={<HomeScreen/>} />
            <Route path='/auth' element={<AuthScreen/>} />
        </Routes>
    )
}

export default AllRoutes