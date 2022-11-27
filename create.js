

const data = [[2, 'Gam cram', 22], [3, 'Mam super', 10], [4, "Sam max", 1]]
// const data = sss1();
for (let index = 0; index < data.length; index++) {
   let createDiv = document.createElement("div");
   createDiv.className = 'personalTable';

   for (let index1 = 0; index1 < data[index].length; index1++) {
      let createSmallDic = document.createElement("div");
      createSmallDic.className = 'infoTable';
      createSmallDic.innerHTML = data[index][index1];
      createDiv.appendChild(createSmallDic);
   }
   let dd = document.querySelector('.containerTable');
   dd.appendChild(createDiv);

}

