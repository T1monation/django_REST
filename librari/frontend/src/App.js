import logo from './logo.svg';
import './App.css';
import React from 'react';
import AuthorList from './components/Author.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBook';
import axios from 'axios';
import { HashRouter, Route, Link, Switch, Redirect, BrowserRouter } from 'react-router-dom'


const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу `{location.pathname}` не найдена</h1>
    </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      'authors': [],
      'books': []
    }
  }
  load_data() {
    axios.get('http://127.0.0.1:8000/api/authors')
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors['results']
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/books')
      .then(response => {
        const books = response.data
        this.setState(
          {
            'books': books['results']
          }
        )
      }).catch(error => console.log(error))
  }

  componentDidMount() {
    this.load_data()
  }

  render() {
    return (
      <div className='App'>
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Authors</Link>
              </li>
              <li>
                <Link to='/books'>Books</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
            <Route exact path='/books' component={() => <BookList items={this.state.books} />} />
            <Route exact path='/author/:id' component={() => <AuthorBookList items={this.state.books} />} />
            <Redirect from='/authors' to='/' />
            <Route component={NotFound404} />
          </Switch>

        </BrowserRouter>

      </div >
    )
  }
}

export default App;