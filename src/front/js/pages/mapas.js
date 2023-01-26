import React, { pages } from "react";
import  GoogleMaps from "simple-react-google-maps";


export const Mapas =() =>{
    
    return(
        <div className="container">
            <GoogleMaps
            apiKey={("AIzaSyB-zFY4ZH0nkE8BZiRH94iFGWJyFgK1MPg")}
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
