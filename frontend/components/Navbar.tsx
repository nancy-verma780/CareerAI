"use client";

import Link from "next/link";
import Logout from "./Logout";


export default function Navbar(){

return (

<nav className="flex justify-between items-center p-5 border-b">

<h1 className="text-2xl font-bold">
CareerAI
</h1>


<div className="flex gap-5">

<Link href="/dashboard">
Dashboard
</Link>


<Link href="/login">
Login
</Link>


<Logout/>

</div>


</nav>

)

}