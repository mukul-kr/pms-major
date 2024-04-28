import React, { useState } from "react";

const RoundCircleDiv = ({ text }) => {
    const [color, setColor] = useState(
        `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(
            Math.random() * 256
        )}, ${Math.floor(Math.random() * 256)})`
    );

    const styles = {
        width: 50,
        height: 50,
        borderRadius: "50%",
        backgroundColor: color,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
    };

    return (
        <div style={styles}>
            <p>{text}</p>
        </div>
    );
};

export default RoundCircleDiv;