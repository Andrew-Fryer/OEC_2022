import './App.css';
import {Route, Switch} from 'react-router-dom';
import Home from './Pages/Home';
import PageNotFound from './Pages/PageNotFound';

function App() {
  return (
    <div className='App'>
      <Switch>
        <Route exact path = '/' render = {props => < Home {...props}/>}/> 
        <Route render ={() => <PageNotFound />} />
      </Switch>
      </div>
  );
}

export default App;
