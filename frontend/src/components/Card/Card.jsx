import React from 'react';
import { Card, CardContent, CardHeader, Typography, Avatar } from '@material-ui/core';

const CardComponent = ({ name, id, password }) => {
    const profilePic = name.charAt(0).toUpperCase();
    console.log(profilePic)
    return (
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
                    Security: {password}
                </Typography>
            </CardContent>
        </Card>
    );
};

export default CardComponent;