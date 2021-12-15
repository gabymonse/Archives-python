#---------------CLASE NODO-------
class Node:
      def __init__(self, value, next_node=None):
       self.value = value
       self.next_node = next_node
    
      def get_value(self):
       return self.value
  
      def get_next_node(self):
       return self.next_node
  
      def set_next_node(self, next_node):
       self.next_node = next_node

#---------------CLASE LINKED LIST--------
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
#PARA AÑADIR UN NODO (AL PRINCIPIO POR QUE ASI ES LINKED LISTS)
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
#PARA SACAR LOS VALUES DE MIS NODOS EN FORMA DE STRINGS ( TODOS EN ORDEN)
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
#PARA REMOVER NODOS (SE REMUEVE EL PRIMER NODO QUE APAREZCA QUE TENGA EL VALUE QUE DIJE -VALUE_TO_REMOVE-)
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node