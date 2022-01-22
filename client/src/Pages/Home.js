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
                latitude: 54,
                longitude: 4,
                type: "waste",
                amount: 10000,
                risk:  111,
            },
            {
                id: 2,
                latitude: -25,
                longitude: 5,
                type: "regional_sorting_facility",
                amount: 10000,
                risk:  111,
            },
            {
                id: 3,
                latitude: -25,
                longitude: 85,
                type: "regional_recycling_facility",
                amount: 10000,
                risk:  111,
            },
            {
                id: 4,
                latitude: -50,
                longitude: 5,
                type: "local_sorting_facility",
                amount: 10000,
                risk:  111,
            },
            {
                id: 5,
                latitude: -25,
                longitude: 125,
                type: "local_recycling_facility",
                amount: 10000,
                risk:  111,
            },
            {
                id: 6,
                latitude: -75,
                longitude: 5,
                type: "unknown",
                amount: 10000,
                risk:  111,
            }
        ],
        route:[
            {
                startLat: -25,
                startLng: 5,
                startType:"regional_sorting_facility",
                endLat: -50,
                endLng: 5,
                endType:"local_sorting_facility",
                distance: 10,
            },
            {
                startLat: 54,
                startLng: (Math.random() - 0.5) * 360,
                startType:"waste",
                endLat: (Math.random() - 0.5) * 180,
                endLng: (Math.random() - 0.5) * 360,
                endType:"local_sorting_facility",
                distance: 10,
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
                pointLat={(point) => point.lat || point.latitude}
                pointLng={(point) => point.lng || point.longitude}
                onPointHover={(point) => setCurrentPoint(point)}
                pointColor={(point) => markerColors[point.type] || "#4dabf5"}
                arcsData={data.route}
                arcDashGap={() => .2}
                arcDashAnimateTime={() => 2500}
                arcColor={(data) => [markerColors[data.startType], markerColors[data.endType]]}
            />
        </div>
    );
}

export default Home;