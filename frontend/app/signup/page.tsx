"use client";

import {supabase} from "@/lib/supabase";
import {useState} from "react";


export default function Signup(){

const [email,setEmail]=useState("");
const [password,setPassword]=useState("");


async function signup(){

const {error}=await supabase.auth.signUp({

email,

password

});


if(error){

alert(error.message)

}
else{

alert("Signup successful")

}

}


return (

<div className="p-10">

<h1 className="text-3xl font-bold">
Create Account
</h1>


<input
className="border p-2 mt-5 block"
placeholder="Email"
onChange={
e=>setEmail(e.target.value)
}
/>


<input
className="border p-2 mt-5 block"
placeholder="Password"
type="password"
onChange={
e=>setPassword(e.target.value)
}
/>


<button
className="mt-5 bg-black text-white p-3"
onClick={signup}
>
Signup
</button>


</div>

)

}