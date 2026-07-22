"use client";

import { supabase } from "@/lib/supabase";
import { useState } from "react";
import { useRouter } from "next/navigation";


export default function Login(){

const router = useRouter();

const [email,setEmail]=useState("");
const [password,setPassword]=useState("");


async function login(){

const {error}=await supabase.auth.signInWithPassword({

email,

password

});


if(error){

alert(error.message);

}
else{

router.push("/dashboard");

}

}


return (

<div className="p-10">


<h1 className="text-3xl font-bold">
Login
</h1>


<input

className="border p-2 block mt-5"

placeholder="Email"

onChange={
e=>setEmail(e.target.value)
}

/>


<input

className="border p-2 block mt-5"

placeholder="Password"

type="password"

onChange={
e=>setPassword(e.target.value)
}

/>


<button

className="bg-black text-white p-3 mt-5"

onClick={login}

>

Login

</button>


</div>

)

}