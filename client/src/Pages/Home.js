import React, {useState} from 'react';
import Globe from 'react-globe.gl';
import GlobeHeader from '../Components/GlobeHeader';
import InputParams from '../Components/InputParams';
import Results from '../Components/Results';

const Home = (props) => {

    const {markerColors} = props;

    const [currentPoint, setCurrentPoint] = useState(null);

    const [data, setData] = useState(false);

    const getPointRadius = (point) => {
        // if start or end node
        if (point.id === data.points[0].id || point.id === data.points[data.points.length-1].id) return 0.75

        // else 
        return 0.25;
    }
   
    return (
        <div>
            {/* TODO change myData to data */}
            <InputParams id="/input" onSetData={(data) => setData(data)} />
            {data &&
            <>
                <GlobeHeader id="/globe" markerColors={markerColors} currentPoint={currentPoint} />
                <Globe
                    id="/results"
                    globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
                    pointsData={data.points}
                    pointRadius={(point) => getPointRadius(point)}
                    pointAltitude={(point) => point.id === data.points[0].id ? .1 : .05}
                    pointLat={(point) => point.lat || point.latitude}
                    pointLng={(point) => point.lng || point.longitude}
                    onPointHover={(point) => setCurrentPoint(point)}
                    pointColor={(point) => markerColors[point.type] || "#4dabf5"}
                    arcsData={data.route}
                    arcDashGap={() => .2}
                    arcDashAnimateTime={() => 2500}
                    arcColor={(data) => [markerColors[data.startType], markerColors[data.endType]]}
                />
                <Results data={data.data} />
            </> }
        </div>
    );
}

export default Home;