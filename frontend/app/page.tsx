export default function Home(){

return (

<div className="min-h-screen p-10">


<h1 className="text-6xl font-bold">

CareerAI

</h1>


<p className="text-xl mt-5">

AI powered career intelligence platform for students.

</p>



<div className="mt-10">

<a

href="/signup"

className="bg-black text-white px-6 py-3 rounded"

>

Start Your Career Analysis

</a>


</div>



<div className="grid md:grid-cols-3 gap-5 mt-20">


<div className="p-5 shadow rounded">

<h2 className="font-bold text-xl">

Resume AI Analysis

</h2>

<p>

Analyze skills and improve your resume.

</p>

</div>




<div className="p-5 shadow rounded">

<h2 className="font-bold text-xl">

Career Prediction

</h2>

<p>

Find the best career path.

</p>

</div>





<div className="p-5 shadow rounded">

<h2 className="font-bold text-xl">

AI Mentor

</h2>

<p>

Get personalized guidance.

</p>

</div>


</div>


</div>

)

}