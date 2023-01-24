import React, { pages } from "react";
import  GoogleMaps from "simple-react-google-maps";

// const key = process.env.API_MAPS
console.log(key)
export const Mapas =() =>{
    
    return(
        <div className="container">
            <GoogleMaps
            apiKey= {key}
            style={{height : "500px", width: "290px"}}
            zoom={15}
            center={{
                lat: -33.5070426,
                lng: -70.6609057,
            }}
         />
        </div>
    )
}
