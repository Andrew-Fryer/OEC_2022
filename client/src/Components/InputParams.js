/**
 * This file uses code from a heavily modified sign in template; link below:
 * https://github.com/mui-org/material-ui/blob/master/docs/src/pages/getting-started/templates/sign-in/SignIn.js
 */
import React, {useEffect, useState} from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Select from '@mui/material/Select';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import MenuItem from '@mui/material/MenuItem';

const InputParams = (props) => {

  const [csvFiles, setCSVFiles] = useState([]);
  const [selectedCSVFile, setSelectedCSVFile] = useState(0);

  // TODO disable form changes when loading

  useEffect(() => {
    async function getCSVFiles() {
      // TODO: HIT BACKEND
      // const res = await fetch('/api/files', {
      //   method: 'GET',
      // });
      // const resBody = await res.json();
      // setCSVFiles(resBody.files);
      setCSVFiles(["csv1","csv2","csv3","csv4"]);
    }
    getCSVFiles();
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // TODO: HIT BACKEND
    console.log({
      a: data.get('a'),
      b: data.get('b'),
      csv: csvFiles[selectedCSVFile],
    });
  };

  const handleChange = (event) => {
    console.log(event.target.value);
    setSelectedCSVFile(event.target.value);
  }

  return (
    <Box m={5}>
      <Typography component="h1" variant="h5">
        Enter Algorithm Parameters
      </Typography>
      <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
        <Grid container spacing={2}>
          <Grid item xs={3}>
            <TextField margin="normal" required fullWidth id="email" label="a" name="a" autoFocus />
          </Grid>
          <Grid item xs={3}>
            <TextField margin="normal" required fullWidth name="b" label="b" id="password" />
          </Grid>
          <Grid item xs={6}>
            {csvFiles ? 
            <Select 
              value={selectedCSVFile}
              onChange={handleChange}
              label="Select CSV File"
            >
              {csvFiles.map((fileName, index) => <MenuItem value={index}>{fileName}</MenuItem>)}
            </Select>
            : "Getting CSV Files"
          }
          </Grid>
          <Grid item xs={12}>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Submit
            </Button>
          </Grid>
        </Grid>
      </Box>
    </Box>
  );

}

export default InputParams;