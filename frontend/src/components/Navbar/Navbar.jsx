import React from "react";
import '../Navbar/Navbar.css'
import { Link } from "react-router-dom";
import logo from "./../../assets/images/logo.ico"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faBars} from "@fortawesome/free-solid-svg-icons";

const Navbar = (props) => {
    library.add(faBars)
    return(
        <div>
            <div className="navbar">
                <div className="logo">
                    
                </div>
                <div className="menu-icon-mobile" onClick={(e) => {props.menuData.setMobileNav(!props.menuData.mobileNav)}}>
                    <FontAwesomeIcon icon="fa-solid fa-bars" />
                </div>
                <div className="nav-btns">
                    <Link>About</Link>
                    <Link to="/auth">Signup</Link>
                    <Link to="/auth">Login</Link>
                </div>
            </div>
        </div>
    )
}

export default Navbar