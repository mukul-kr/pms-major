import React from 'react';
import { Card, CardContent, CardHeader, Typography, Avatar } from '@material-ui/core';

const SensorCardComponent = ({ name, id, sensorAlertValue, sensorAlertDirection, upperRangeAlertValue, lowerRangeAlertValue }) => {
    const profilePic = name.charAt(0).toUpperCase();
    console.log(profilePic)
    return (
        <>
            <Card>
                <CardHeader
                    avatar={
                        <Avatar aria-label="profile picture">
                            {profilePic}
                        </Avatar>
                    }
                    title={name}
                />
                <CardContent>
                    <Typography variant="body2" component="p">
                        ID: {id}
                    </Typography>
                    <Typography variant="body2" component="p">
                        Alert Type: {sensorAlertDirection}
                    </Typography>
                    {sensorAlertDirection != 'Value Between range is Better' ? (
                        <Typography variant="body2" component="p">
                            Alert Value: {sensorAlertValue}
                        </Typography>
                    ) : (
                        // Your else part here
                        <>
                            <Typography variant="body2" component="p">
                                Lower Alert Value: {lowerRangeAlertValue}
                            </Typography>
                            <Typography variant="body2" component="p">
                                Upper Alert Value: {upperRangeAlertValue}
                            </Typography>
                        </>
                    )}


                </CardContent>
            </Card>
            <br />
        </>
    );
};

export default SensorCardComponent;