const User = require("../models/user");

const resolvers = {
  Query: {
    getAllUsers: async () => {
      return await User.find();
    },
    getUserById: async (_, { id }) => {
      return await User.findById(id);
    },
  },
  Mutation: {
    createUser: async (_, { name, email, password }) => {
      const newUser = new User({ name, email, password });
      await newUser.save();
      return newUser;
    },
    updateUser: async (_, { id, name, email, password }) => {
      const updatedUser = await User.findByIdAndUpdate(
        id,
        { name, email, password },
        { new: true, runValidators: true }
      );
      return updatedUser;
    },
    deleteUser: async (_, { id }) => {
      const deleted = await User.findByIdAndDelete(id);
      return deleted !== null; // Retorna `true` si se eliminó, `false` si no se encontró
    },
  },
};

module.exports = resolvers;
