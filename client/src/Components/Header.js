import React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import Toolbar from '@mui/material/Toolbar';

const Header = () => {
    return (
        <AppBar position="sticky">
            <Toolbar>
                <Button style={{color:"white"}} disabled>TEAM SONIC: WASTE MAP-TRACKER</Button>
            </Toolbar>
        </AppBar>
    );
};

export default Header;