function swap(buildquestion1, buildquestion2) {
	document.getElementById(buildquestion1).style.display = 'block';
	document.getElementById(buildquestion2).style.display = 'none';
}
document.getElementById('next').addEventListener('click',function(e){
	swap('buildquestion1','buildquestion2');
});
document.getElementById('bt2').addEventListener('click',function(e){
	swap('buildquestion2','buildquestion1');
});