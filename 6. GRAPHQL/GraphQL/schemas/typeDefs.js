const { gql } = require("apollo-server-express");

const typeDefs = gql`
  # Definiciones de tipo para el modelo de usuario
  type User {
    id: ID!
    name: String!
    email: String!
    password: String! # Normalmente, las contraseñas no se devuelven, pero para fines de ejemplo
    createdAt: String
    updatedAt: String
  }

  # Consultas para obtener datos
  type Query {
    getAllUsers: [User!]!
    getUserById(id: ID!): User
  }

  # Mutaciones para crear, actualizar y eliminar datos
  type Mutation {
    createUser(name: String!, email: String!, password: String!): User
    updateUser(id: ID!, name: String, email: String, password: String): User
    deleteUser(id: ID!): Boolean
  }
`;

module.exports = typeDefs;
