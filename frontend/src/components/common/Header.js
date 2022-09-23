import React from "react";
// import header from "../../assets/header2.jpg";
// import Typewriter from "typewriter-effect";
import Button from '@mui/material/Button';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
function Header() {
  return (

    <div
      style={{
        backgroundImage: `linear-gradient(rgba(0,0,0,.7), rgba(0,0,0,.3)), url(https://gradely.ng/wp-content/themes/gradely/img/banners/gradely_girl.png})`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center center",
        height: "100vh",
        paddingTop: "50px",
      }}
    >
      <div 
        style={{
          marginTop: "8rem",
          paddingLeft: '10%'
        }}
      >
        <p className="text-white  italic font-bold text-4xl">
            Personalised Learning
        </p>
        <p className="text-white italic text-4xl mt-3">
            at home and in school
        </p>
        <Button variant="contained" color="success" size='large' sx={{mt:5, borderRadius:50, fontWeight:'bold', mx:5}}> 
        Start Here
      </Button>
        
      </div>
    </div>  
    
  );
}

export default Header;