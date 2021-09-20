--Exercise 1
--1.1
-- SELECT CustomerID, CompanyName, Address, City, Region, PostalCode, Country FROM Customers
-- WHERE City IN ('Paris', 'London');

--1.2
-- SELECT * FROM Products
-- WHERE RIGHT(QuantityPerUnit, 7) = 'bottles';

--1.3
-- SELECT ProductName, Suppliers.CompanyName, Suppliers.Country FROM Products
-- JOIN Suppliers
-- ON Suppliers.SupplierID = Products.SupplierID
-- WHERE RIGHT(QuantityPerUnit, 7) = 'bottles';

-- 1.4
-- SELECT c.CategoryName, COUNT(*) AS 'Quantity of Products' FROM Products p 
-- INNER JOIN Categories c
-- ON p.CategoryID = c.CategoryID
-- GROUP BY c.CategoryName
-- ORDER BY [Quantity of Products] DESC;

--1.5
-- SELECT TitleOfCourtesy + ' ' + FirstName + ' ' + LastName AS 'Employee', City
-- FROM Employees
-- WHERE Country = 'UK';

-- 1.6
-- SELECT COUNT(*) FROM Orders
-- WHERE ShipCountry IN ('USA', 'UK') AND Freight > 100.00;

-- 1.7
-- SELECT OrderID, UnitPrice*Quantity AS 'Un-discounted Price', (1-Discount)*UnitPrice*Quantity AS 'Amount of Discount' FROM [Order Details Extended] ode
-- ORDER BY [Amount of Discount] DESC; 

-- OR 1.7
-- SELECT TOP 1 OrderID FROM [Order Details Extended] ode
-- ORDER BY ((1-Discount)*UnitPrice*Quantity) DESC; 