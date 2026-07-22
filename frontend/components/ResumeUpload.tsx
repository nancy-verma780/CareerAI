"use client";

import { useState } from "react";


export default function ResumeUpload(){

    const [file,setFile] = useState<File | null>(null);


    async function uploadResume(){

        if(!file){
            alert("Please select a file");
            return;
        }


        const formData = new FormData();

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


        const data = await response.json();

        console.log(data);

    }


    return (

        <div className="mt-10">

            <input
            type="file"
            onChange={(e)=>
                setFile(
                    e.target.files?.[0] || null
                )
            }
            />


            <button
            onClick={uploadResume}
            className="ml-4 bg-black text-white px-5 py-2 rounded"
            >

            Analyze Resume

            </button>

        </div>

    )

}