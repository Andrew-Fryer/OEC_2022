import React from 'react';
import Globe from 'react-globe.gl';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
const Home = () => {
    const myData=[
        {
            id: 1,
            name: "plant1",
            lat: (Math.random() - 0.5) * 180,
            lng: (Math.random() - 0.5) * 360,
            type: "recycling",
            plastic: 10000,
            risk:  111,
        }
    ]
    return (
        <div>
            <Box style={{position: "absolute", backgroundColor: "white"}}>
                <Typography>Point Data</Typography>
                <Typography>Latitude:</Typography>
                <Typography></Typography>
            </Box>
            <Globe
                pointsData={myData}
                onPointHover={(point, prevPoint) => {
                    console.log(point)
                    console.log(prevPoint)
                }}
                onPointClick={(point) => console.log(point)}
            />
        </div>
    );
}

export default Home;