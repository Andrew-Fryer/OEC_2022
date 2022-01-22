import React from 'react';
import { useHistory, Link } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

const Header = (props) => {
    const history = useHistory();
    return (
        <AppBar position="sticky">
            <Toolbar>
                <Button color="inherit"><Typography color="inherit"><href to="input">Enter Parameters</href></Typography></Button>
                <Button color="inherit"><Typography color="inherit"><href to="/globe">Globe</href></Typography></Button>
                <Button color="inherit"><Typography color="inherit">
                    <href to="/results">Results</href>
                    </Typography></Button>
            </Toolbar>
        </AppBar>
    );
};

export default Header;