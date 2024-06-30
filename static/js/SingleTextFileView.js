const copyBtn=document.getElementById("copy");
const noteContent=document.getElementById("NoteContent");
copyBtn.addEventListener("click",()=>{
    window.navigator.clipboard.writeText(noteContent.value);
})