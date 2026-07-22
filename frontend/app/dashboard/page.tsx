"use client";

import Logout from "@/components/logout";
import { supabase } from "@/lib/supabase";
import router from "next/dist/shared/lib/router/router";
import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import Navbar from "@/components/Navbar";
useEffect(()=>{

async function loadData(){

const {
data:{
session
}

}= await supabase.auth.getSession();


if(!session){

router.push("/login");

return;

}


const response = await fetch(
`http://127.0.0.1:8000/history/${session.user.email}`
);


const result = await response.json();


setHistory(result);


}


loadData();


},[router]);


export default function Dashboard(){

const router = useRouter();

const [data,setData] = useState<any>(null);
const [history,setHistory] = useState<any[]>([]);


useEffect(()=>{

async function checkUser(){

const {
data:{
session
}

}= await supabase.auth.getSession();


if(!session){

router.push("/login");

}

}


checkUser();

},[router]);



async function upload(e:any){

const file=e.target.files[0];


const formData=new FormData();

formData.append(
"file",
file
);


const response = await fetch(
"http://127.0.0.1:8000/upload-resume",
{
method:"POST",
body:formData
}
);
<div className="min-h-screen">

<Navbar/>

<div className="p-10"></div>

const result = await response.json();

setData(result);

}


<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Previous Resume Analysis
</h2>


{
history.map(
(item:any)=>(

<div key={item.id} className="mt-3">

<p>
Score: {item.score}/100
</p>

<p>
Career:
{item.career?.recommended_role}
</p>

</div>

)

)

}

</div>
return (

<div className="min-h-screen p-10">


<div className="flex justify-between items-center">

<h1 className="text-4xl font-bold">
CareerAI Dashboard
</h1>

<Logout/>

</div>



<input

type="file"

className="mt-10"

onChange={upload}

/>



{
data && (

<div className="mt-10 grid gap-6">



{/* Resume Score */}

<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Resume Score
</h2>

<p className="text-3xl font-bold">

{data.resume_score}/100

</p>

</div>




{/* Skills */}

<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Skills
</h2>


<div className="flex gap-2 flex-wrap mt-3">

{

data.skills.map(

(skill:string)=>(

<span

key={skill}

className="bg-blue-100 px-3 py-1 rounded"

>

{skill}

</span>

)

)

}

</div>

</div>





{/* Career */}

<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Recommended Career
</h2>


<p className="text-2xl font-bold">

{data.career.recommended_role}

</p>


<p>

Match Score:

{data.career.match_score}

</p>


</div>





{/* Roadmap */}

<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Learning Roadmap
</h2>


{

data.roadmap.map(

(item:string)=>(

<p key={item}>

{item}

</p>

)

)

}


</div>





{/* Projects */}

<div className="p-5 rounded shadow">

<h2 className="text-xl font-bold">
Recommended Projects
</h2>


{

data.recommended_projects.map(

(item:string)=>(

<p key={item}>

{item}

</p>

)

)

}


</div>




</div>

)

}



</div>

)

}