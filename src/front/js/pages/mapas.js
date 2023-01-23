import React, { pages } from "react";
import  GoogleMaps from "simple-react-google-maps";

export const Mapas =() =>{
    return(
        <div className="container">
            <GoogleMaps
            style={{height : "500px", width: "370px"}}
            zoom={10}
            center={{
                lat: 9.427374,
                lng: -1.666874,
            }}
         />
        </div>
    )
}
