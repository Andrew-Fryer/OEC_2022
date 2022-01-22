import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { makeStyles } from "@material-ui/core/styles";

// logo styling
const useStyles = makeStyles((theme) => ({
    results: {
        color: "white",
        backgroundColor: "black"
    },
}));


const Results = (props) => {
    const classes = useStyles();
    const {data} = props;
    
    return (
        <Box spacing={2} className={classes.results}> 
            <Typography variant="h5" color="inherit">Results</Typography>
            <Grid container spacing={2}>
                <Grid item xs={6}>
                    <Typography color="inherit"><b>QoR: </b>{data.QoR}</Typography>
                    <Typography color="inherit"><b>Total Distance: </b>{data.totalDistance}</Typography>
                    <Typography color="inherit"><b>Total Plastic in Ocean: </b>{data.totalPlasticInOcean}</Typography>
                </Grid>
                <Grid item xs={6}>
                    <Typography color="inherit"><b>Total Plastic Lost: </b>{data.totalPlasticLost}</Typography>
                    <Typography color="inherit"><b>Total Plastic Produced: </b>{data.totalPlasticProduced}</Typography>
                    <Typography color="inherit"><b>Total Plastic Recycled: </b>{data.totalPlasticRecycled}</Typography>
                </Grid>
            </Grid>
        </Box>
    );
};

export default Results;