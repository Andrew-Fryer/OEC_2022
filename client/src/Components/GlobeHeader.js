import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { makeStyles } from "@material-ui/core/styles";

// logo styling
const useStyles = makeStyles((theme) => ({
    pointData: {
        color: "white",
        backgroundColor: "black"
    },
}));

const GlobeHeader = (props) => {
    const {markerColors, currentPoint} = props;
    const classes = useStyles();


    const PointDataField = (props) => {
        const {fieldName, description} = props;
        if (fieldName === "risk") return <Typography color="primary"><b>{description}</b>: {currentPoint ? currentPoint.risk +"%" : "Nothing Selected"}</Typography>
        return <Typography color="primary"><b>{description}</b>: {currentPoint ? currentPoint[fieldName] : "Nothing Selected"}</Typography>
    }

    return (
        <Box>
            <Grid container className={classes.pointData}>
                {/* TODO FIX POINT DATA DISPLAY OR REMOVE */}
                <Grid item container xs={9}>
                    <Grid item xs={12}>
                        <Typography variant="h5">Point Data</Typography>
                    </Grid>
                    <Grid item xs={4}>
                        <PointDataField fieldName="id" description="ID"/>
                        <PointDataField fieldName="latitude" description="Latitude"/>
                    </Grid>
                    <Grid item xs={4}>
                        <PointDataField fieldName="longitude" description="Longitude"/>
                        <PointDataField fieldName="type" description="Facility Type"/>
                    </Grid>
                    <Grid item xs={4}>
                        <PointDataField fieldName="amount" description="Plastic Amount"/>
                        <PointDataField fieldName="risk" description="Risk Level"/>
                    </Grid>
                </Grid>
                <Grid item container xs={3}>
                    <Grid item xs={12}>
                        <Typography variant="h5">Legend</Typography>
                    </Grid>
                    {/* TODO ADD LEGEND */}
                    {/* {markerColors.map((color, index) => index)} */}
                </Grid>
            </Grid>
        </Box>
    )

}

export default GlobeHeader;