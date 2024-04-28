import React from "react";
import '../UsernameMenu/UsernameMenu.css'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faRightFromBracket} from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
import api from "../../api/api";

const UsernameMenu = () => {
    library.add(faUser,faRightFromBracket)

    const navigate = useNavigate()

    const handleLogout = () => {
        console.log("clicked")
        api.delete("/auth/logout",{
            headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        }).then(response => {
            console.log(response.status)
            navigate("/")
        })
    }
    return(
        <div className="flex flex-col dropdownProfile">
            <div>
                <div className="menu-item" onClick={()=> {navigate("/user-profile")}}>
                    <FontAwesomeIcon icon="fa-solid fa-user" />
                    <p>Profile</p>
                </div>
                <div className="menu-item" onClick={handleLogout}>
                    <FontAwesomeIcon icon="fa-solid fa-right-from-bracket" />
                    <p>Logout</p>
                </div>
            </div>
        </div>
    )
}

export default UsernameMenu