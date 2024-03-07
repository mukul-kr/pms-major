import React from "react";
import '../AuthScreen/AuthScreen.css'
import bg from './../../assets/images/auth1.png'
import loginBg from './../../assets/images/login.svg'
import { MDBBtn, MDBInput } from 'mdb-react-ui-kit';
import { useState } from "react";
import api from "../../api/api";
import { useNavigate } from "react-router-dom";
import { error } from "highcharts";
import ParticlesEffect from "../../components/Particles/ParticleEffect";

const AuthScreen = () => {
    const [displayLogin, setDisplayLogin] = useState("block")
    const [displayRegister, setDisplayRegister] = useState("none")

    const [email, setEmail] = useState()
    const [fullName, setFullName] = useState()
    const [organisation, setOrganisation] = useState()
    const [password, setPassword] = useState()
    const [cpassword, setcpassword] = useState()
    const [phone, setPhone] = useState()

    const [username, setUsername] = useState()
    const [loginPassword, setloginPassword] = useState()
    const navigate = useNavigate()

    const handleLoginSubmit = (e) => {
        e.preventDefault()
        document.cookie = `token=; path=/`;

        api.post('/auth/login',{
            "username":username,
            "password":loginPassword
        }
        ,{
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        }
        ).then(response => {
            console.log(response.data)
            if(response.status == 200){
                localStorage.setItem("name" , response.data.username)
                document.cookie = `token=${response.data.access_token}; path=/`;
                navigate("/analytics")
            }
        }).catch(error => {
            console.log(error)
        })

        console.log(username,loginPassword)
    }

    const handleRegisterSubmit = (e) => {
        e.preventDefault()
        if(password !== cpassword){
            alert("passwords didn't match")
            return
        }
        if(phone.trim().length != 10){
            alert("phone number must be of 10 letters")
            return
        }
        else{
            api.post('/auth/signup',{
                "email":email,
                "organisation":organisation,
                "phone_number": phone,
                "full_name": fullName,
                "password" : password
            },{
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            }}
            ).then(response => {
                console.log(response.data)
                if(response.status == 200){
                    alert("user registered successfully")
                    var inputs = document.getElementsByClassName('form-control')
                    for(var i=0; i<inputs.length;i++){
                        inputs[i].value = ""
                    }
                }
            }).catch(error => {
                alert(error.response.data.detail)
            })
        }
        console.log(email)
        console.log(fullName)
        console.log(organisation)
        console.log(password)
        console.log(cpassword)
    }

    const handleDisplayLogin =()=> {
        setDisplayLogin("block")
        setDisplayRegister("none")
    }

    const handleDisplayRegister = () => {
        setDisplayLogin("none")
        setDisplayRegister("block")
    }
    return(
        <div className="AuthPage">
            <ParticlesEffect />
            <div className="AuthCard">
                <div className="image-div">
                    <img className="shape-bg" src={bg}/>
                    <img className="login-bg" src={loginBg}/>
                </div>
                <div className="form-div">
                    <h2 className="form-header">Welcome!</h2>
                    <center>
                    <div className="login-signup-btns">
                        <h4 onClick={handleDisplayLogin} className={displayLogin == "block" ? "selected-btn":""}>Login</h4>
                        <h4 onClick={handleDisplayRegister} className={displayRegister == "block" ? "selected-btn":""}>Signup</h4>
                    </div>
                    </center>
                    <div className="login-div" style={{display: displayLogin}}>
                        <form className="login-form" onSubmit={handleLoginSubmit}>
                            <MDBInput label='Username' id='username' type='text' size="lg" name="username" required onChange={(e)=> {setUsername(e.target.value)}}/>
                            <MDBInput label='Password' id='login_password' type='password' size="lg" name="password"  required onChange={(e) => {setloginPassword(e.target.value)}}/>
                            <p className="forgot-password">Forgot password ?</p>
                            <MDBBtn>Submit</MDBBtn>
                        </form>
                    </div>
                    <div className="signup-div" style={{display: displayRegister}}>
                        <form className="signup-form" onSubmit={handleRegisterSubmit}>
                            <MDBInput label='Full Name' id='fullname' type='text' onChange={(e) => {setFullName(e.target.value)}} required />
                            <MDBInput label='Email' id='email' type='email' onChange={(e) => {setEmail(e.target.value)}} required />
                            <MDBInput label='Phone Number' id='phone' type='text' onChange={(e) => {setPhone(e.target.value)}} required />
                            <MDBInput label='Organization' id='organization' type='text' onChange={(e) => {setOrganisation(e.target.value)}} required />
                            <MDBInput label='Password' id='password' type='password' onChange={(e) => {setPassword(e.target.value)}} required />
                            <MDBInput label='Confirm Password' id='confirmPassword' type='password' onChange={(e) => {setcpassword(e.target.value)}} required  />
                            <MDBBtn>Submit</MDBBtn>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AuthScreen