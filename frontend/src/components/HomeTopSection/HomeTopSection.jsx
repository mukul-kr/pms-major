import React, { useEffect,useRef  } from "react";
import '../HomeTopSection/HomeTopSection.css'
import Navbar from "../Navbar/Navbar";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faEnvelope,faPhone} from "@fortawesome/free-solid-svg-icons";
import iotImage from "./../../assets/images/iot.png"
import analyticsCard from "./../../assets/images/analytics-card.png"
import sensor from "./../../assets/images/sensors.png"
import shape from "./../../assets/images/bg2.png"
import shape2 from './../../assets/images/mobile_bg.png'
import analyticsImage from './../../assets/images/analytcs2.png'
import featureImage1 from './../../assets/images/ews2.jpg'
import featureImage2 from './../../assets/images/awms2.jpg'
import Zoom from 'react-reveal/Zoom'
import ParticlesEffect from "../Particles/ParticleEffect";
import { useState } from "react";


const HomeTopSection = () => { 
    library.add(faEnvelope, faPhone);
    const [mobileNav, setMobileNav] = useState(false)
    
    return(
        <div className="wrapper" id="wrapper">
            <Navbar menuData = {{mobileNav,setMobileNav}}/>
            <section className="section-1">
                <ParticlesEffect />
                <div className="home-top-section">
                    <div className="intro-text">
                        <p>Pollution</p>
                        <p>Monitoring System</p>
                    </div>
                    <div className="nav-btns-1">
                        <Link href="#section-3">What's New</Link>
                    </div>
                    <div className="shape">
                        <img src={shape}/>
                        <div className="analytics-image">
                            <img src={analyticsImage}/>
                        </div>
                    </div>
                    {/** */}
                    <div className="shape2">
                        <img src={shape} className="shape-img"/>
                        <div className="analytics-image-2">
                            <img src={analyticsImage}/>
                        </div>
                    </div>
                </div>

                <div className="mobile-nav" style={{display: mobileNav == true ? "block" : "none"}}>
                    <Link>About</Link><br/>
                    <Link to="/auth">Signup</Link><br/>
                    <Link to="/auth">Login</Link>
                </div>
            </section>
        </div>

    )
}

export default HomeTopSection