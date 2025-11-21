CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Members;


CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

INSERT INTO Members (member_id, name, email, join_date) VALUES 
(1, 'Alice Smith', 'alice@library.org', '2024-01-01');

INSERT INTO Members (member_id, name, email, join_date) VALUES 
(2, 'Bob Johnson', 'bob@library.org', '2024-02-15');

INSERT INTO Members (member_id, name, email, join_date) VALUES 
(3, 'Charlie Brown', 'charlie@library.org', '2024-03-20');

INSERT INTO Books (book_id, title, author, available) VALUES 
(101, 'The Sun Also Rises', 'Ernest Hemingway', TRUE);

INSERT INTO Books (book_id, title, author, available) VALUES 
(102, 'Pride and Prejudice', 'Jane Austen', FALSE); 

INSERT INTO Books (book_id, title, author, available) VALUES 
(103, '1984', 'George Orwell', TRUE);

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES 
(1, 1, 101, '2025-10-20', NULL); 

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES 
(2, 2, 102, '2025-10-21', '2025-10-28');

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES 
(3, 3, 103, '2025-10-22', NULL);


SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;

SELECT
    B.title,
    B.author,
    L.loan_date
FROM
    Members M
JOIN
    Loans L ON M.member_id = L.member_id
JOIN
    Books B ON L.book_id = B.book_id
WHERE
    M.member_id = 3
    AND L.return_date IS NULL;

UPDATE Books
SET available = FALSE
WHERE book_id = 102;

DELETE FROM Loans
WHERE member_id = 3;

SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;
DESC Members;
DESC Books;
DESC Loans;
