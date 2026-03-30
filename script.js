const container = document.getElementById("container");

historyData.forEach(item=>{
  container.innerHTML += `
    <div class="card" onclick="openDetail('${item.id}')">
      <img src="${item.image}">
      <h3>${item.title}</h3>
    </div>
  `;
});

function openDetail(id){
  window.location = "detail.html?id=" + id;
}
