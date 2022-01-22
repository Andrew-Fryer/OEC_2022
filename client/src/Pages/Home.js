import React, {useState} from 'react';
import Globe from 'react-globe.gl';
import GlobeHeader from '../Components/GlobeHeader';
import InputParams from '../Components/InputParams';

const Home = (props) => {

    const {markerColors} = props;

    const [currentPoint, setCurrentPoint] = useState(null);

    const myData =
    {
        points: [
            {
                id: 1,
                lat: 54,
                lng: 4,
                type: "waste",
                plastic: 10000,
                risk:  111,
            },
            {
                id: 2,
                lat: -25,
                lng: 5,
                type: "regional_sorting_facility",
                plastic: 10000,
                risk:  111,
            },
            {
                id: 3,
                lat: -25,
                lng: 85,
                type: "regional_recycling_facility",
                plastic: 10000,
                risk:  111,
            },
            {
                id: 4,
                lat: -50,
                lng: 5,
                type: "local_sorting_facility",
                plastic: 10000,
                risk:  111,
            },
            {
                id: 5,
                lat: -25,
                lng: 125,
                type: "local_recycling_facility",
                plastic: 10000,
                risk:  111,
            },
            {
                id: 6,
                lat: -75,
                lng: 5,
                type: "unknown",
                plastic: 10000,
                risk:  111,
            }
        ],
        route:[
            {
                startLat: (Math.random() - 0.5) * 180,
                startLng: (Math.random() - 0.5) * 360,
                endLat: (Math.random() - 0.5) * 180,
                endLng: (Math.random() - 0.5) * 360,
            },
            {
                startLat: (Math.random() - 0.5) * 180,
                startLng: (Math.random() - 0.5) * 360,
                endLat: (Math.random() - 0.5) * 180,
                endLng: (Math.random() - 0.5) * 360,
            }
        ],
        data: {}
    }
    const [data, setData] = useState(myData);

   
    return (
        <div>
            {/* TODO change myData to data */}
            <InputParams onSetData={(data) => setData(myData)} />
            <GlobeHeader markerColors={markerColors} currentPoint={currentPoint} />

            <Globe
                globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
                pointsData={data.points}
                onPointHover={(point) => setCurrentPoint(point)}
                onPointClick={(point) => setCurrentPoint(point)}
                pointColor={(point) => markerColors[point.type] || "#4dabf5"}
                arcsData={data.route}
                arcDashGap={() => .2}
                arcDashAnimateTime={() => 2500}
            />
        </div>
    );
}

export default Home;