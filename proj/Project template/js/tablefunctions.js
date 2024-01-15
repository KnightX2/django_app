function displayTableData(){
    var html='<table class="table table-bordered" id="VisitorTable" width="100%" cellspacing="0">';
    set T imeout({}=>{
        html+="<thead>";
        html+="<tr>";
        html+="<th >"+"الرقم الوطني"+"</th>";
        html+="<th >"+"الاسم "+"</th>";
        html+="<th >"+"العمر "+"</th>";
        html+="<th >"+"الجنس "+"</th>";
        html+="<th >"+"رقم الهاتف"+"</th>";
        html+="<th >"+"العنوان "+"</th>";
        html+="</tr>";
        html+="</thead>";


    })
}

function addOnClick(){
    var fname=document.getElementById('VisitorFname').value;
    // var mname=document.getElementById('VisitorMname').value;
    // var lname=document.getElementById('VisitorLname').value;
    var nid=document.getElementById('VisitorNID').value;
    var gender=document.getElementById('VisitorGender').value;
    var age=document.getElementById('VisitorAge').value;
    var number=document.getElementById('VisitorNumber').value;
    var address=document.getElementById('VisitorAddress').value;

    if(fname && nid && gender && age && number && address){
        let id=VisitorTable.length+1;
        VisitorTable.push((name:name,nid:nid,gender:gender,age:age,number:number,address:address,id:id));

    }
}