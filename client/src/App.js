import './App.css';
import {Route, Switch} from 'react-router-dom';
import Home from './Pages/Home';
import PageNotFound from './Pages/PageNotFound';
import Header from './Components/Header';


const markerColors = {
  waste: '#ff3d00',
  local_sorting_facility: '#ffee33',
  local_recycling_facility: '#91ff35',
  regional_sorting_facility: '#dd33fa',
  regional_recycling_facility: '#33eaff',
}

function App() {
  return (
    <div className='App'>
      <Header />
      <Switch>
        <Route exact path = '/' render = {props => < Home markerColors={markerColors} {...props}/>}/> 
        <Route render ={() => <PageNotFound />} />
      </Switch>
      </div>
  );
}

export default App;
