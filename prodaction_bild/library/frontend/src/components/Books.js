import React from 'react'
import { Link } from 'react-router-dom'


const BookItem = ({ item, deleteBook }) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.author.first_name}
            </td>
            <td>
                <button onClick={() => deleteBook(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const BookList = ({ items, deleteBook }) => {
    return (
        <div>
            <table>
                <th>
                    ID
                </th>
                <th>
                    Name
                </th>
                <th>
                    Author
                </th>
                {items.map((item) => <BookItem item={item} deleteBook={deleteBook} />)}
            </table>
            <Link to='/books/create'>Create</Link>
        </div>
    )
}
export default BookList
