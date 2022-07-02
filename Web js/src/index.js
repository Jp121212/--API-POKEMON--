// ! npm run build



const fetchPedidos = async () => {
  const data = await fetch('http://127.0.0.1:5000/api/pokemonapi', {
    method: 'GET',
    mode: 'cors'
  });
  
  const PokemonJs = await data.json();
  const lista = document.getElementById("pantalla");
  console.log(PokemonJs)
  Pokemon = PokemonJs.response;



  for (const pokemon of Pokemon) {
    const elementContainer = document.createElement('div');
    const img = document.createElement('div');
    const elementHeader= document.createElement("p");
    const elementSub = document.createElement("p");
    img.innerHTML = `<img src=${pokemon.imagenPerfil} class="img"></img>`;
    elementHeader.innerHTML = `Nombre: ${pokemon.nombre}`;
    elementSub.innerHTML = `Tipo: ${pokemon.tipo}`
    
    
    elementContainer.appendChild(img);
    elementContainer.appendChild(elementHeader);
    elementContainer.appendChild(elementSub);
   
    elementContainer.className = "elementContainer";
    img.className= 'img';


    
    elementContainer.onclick = () => {
      const nombre = document.createElement("p");
      const tipo = document.createElement("p");
      const edad = document.createElement('p');
      const movimientos = document.createElement("p");
      const imagenadc = document.createElement('div');
      const peso = document.createElement('p');
      const descripcion = document.createElement('p');
      const subtitle = document.createElement('p');
      const content = document.getElementById("detalle");
      content.innerHTML = `Descripcion`;
     
      nombre.innerHTML = `Nombre: ${pokemon.nombre}`;
      tipo.innerHTML = `Tipo: ${pokemon.tipo}`;
      edad.innerHTML = `Edad: ${pokemon.edad}`;
      movimientos.innerHTML = `Movimientos: ${pokemon.movimientos}`;
      imagenadc.innerHTML = `<img src=${pokemon.imagenadc} class="img1"></img>`;
      peso.innerHTML = `Peso: ${pokemon.peso} kg`; 
      subtitle.innerHTML = `Curiosidades:`;
      descripcion.innerHTML = `${pokemon.descripcion}`;
      
      content.appendChild(document.createElement("hr"));
      content.appendChild(nombre);
      nombre.appendChild(tipo);
      tipo.appendChild(edad);
      edad.appendChild(movimientos);
      movimientos.appendChild(peso);
      peso.appendChild(imagenadc);
      imagenadc.appendChild(subtitle);
      subtitle.appendChild(descripcion);



     

     

     
     
    };
    lista.appendChild(elementContainer);
  }

}
fetchPedidos();




