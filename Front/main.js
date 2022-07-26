// My server URL
const MY_SERVER = "http://127.0.0.1:8000/";

//   getdata - with out display
const getAllBooks = async () => {
  const token = localStorage.getItem("token");
  let cart = await axios(MY_SERVER + "allthebooks");

  return cart.data;
};

let Books = [];
//   build display (inside a div)
const buildDisplay = async () => {
  Books = await getAllBooks();

  mydisplay.innerHTML =
    "<h1>All the Books</h1><div class='row row-cols-1 row-cols-md-5 g-4'> <br>" +
    Books.map(
      (item, ind) => `<div> 
        <div class="col">
          <div class="card h-100">
          <img src="${MY_SERVER + "media/" + item.image}" class="card-img-top" alt="...">
          <div class="card-body">
              <h5 class="card-title">${item.title} </h5>
              <h6 class="card-subtitle mb-2 text-muted">Author: ${item.author} <br>Genre: ${item.genre}</h6>
              <p class="card-text">${item.desc} <br><button class="btn btn-success" onclick="loan(${item.id})">Add</button></p>
          </div>
          </div>
          </div>
        </div>`
    ).join("") +
    "</div>";
};

const register = async () => {
  const myData = {
    username: username.value,
    password: password.value,
    email: email.value,
  };
  let res = await axios.post(MY_SERVER + "register", myData);
  console.log(res.data);
};

const login = async () => {
  const myData = {
    username: username.value,
    password: password.value,
  };

  let res = await axios.post(MY_SERVER + "login", myData);
  console.log(res.data);
  localStorage.setItem("token", res.data.access);
};

const loan = async (id) => {
  console.log(id);

  // check if user logged
  const token = localStorage.getItem("token");
  if (!token) {
    //exit from function if the user not logged
    msg.innerHTML = "<h1>Please login first";
    return;
  }
  const myData = {
    b_id: id,
  };

  console.log(myData);
  let res = await axios.post(MY_SERVER + "loan", myData, {
    headers: { Authorization: `Bearer ${token}` },
  });
  console.log(res.data);
};

const getMyBooks = async () => {
  const token = localStorage.getItem("token");
  if (!token) {
    //exit from function if the user not logged
    msg.innerHTML = "<h1>Please login first";
    return;
  }
  let cart = await axios(MY_SERVER + "mybooks", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  
  cart = cart.data
  console.log(cart)
  myBooksCart.innerHTML =  "<h1>My loaned books</h1> <br> <div class='row row-cols-1 row-cols-md-2 g-4' style='max-width: 540px;'>" +
  cart.map(
      (item) => `<div class="row g-0">
      <div class="col-md-4">
        <img src="${MY_SERVER + "media/" + item.image}" class="img-fluid rounded-start" alt="...">
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">${item.title}</h5>
          <p class="card-text">${item.desc}</p>
          <p class="card-text"><small class="text-muted">Loan date: ${(item.createdTime).slice(0, 10)}</small></p>
        </div>
      </div>
    </div>`
    )
    .join("") + "</div><br>";
  
};

// try to make a return book date
/* const getDate = (date) => {
  dateDay = parseInt((date.slice(8, 10))) + 15
  dateMonth = date.slice(5, 7)
  dateYear = date.slice(0, 4)
  
  console.log(dateDay, dateMonth, dateYear)
} */
{/* <div class='card mb-3' style='max-width: 540px;'>
  <div class="row g-0">
    <div class="col-md-4">
      <img src="https://picsum.photos/20${item._id}" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">${item.title}</h5>
        <p class="card-text">${item.desc}</p>
        <p class="card-text"><small class="text-muted">${item.createdTime}</small></p>
      </div>
    </div>
  </div>
</div> */}