from typing import Any, Type
from typing_extensions import Self  # pip install typing_extensions


class LinkedStack:
    """LIFO Stack implemenation using a singly linked list for storage."""

    class _Node:
        """Non-public class for storing a singly linked list node."""

        def __init__(self: Self, val: Any, link: Self | None = None) -> None:
            """Create and initilize an object that can be used as node to build
            a singly linked list.

            Args:
                self (Self): An object.
                val (Any): The data object stored inside the node.
                link (Self, optional): Reference to next node object in singly
                linked list. Defaults to None.
            """
            self._val = val
            self._link = link

        @classmethod
        def _valid_link(cls: Type[Self], link: Self | None) -> bool:
            """Validate the link.

            Args:
                cls (Type[Self]): A class object.
                link (Self | None): This is link that need be validate. In order
                link to be valid it need to be either LinkedStack._Node or None
                type.

            Returns:
                bool: Return True, when link is valid, False otherwise.
            """
            return isinstance(link, cls) or link is None

        @property
        def _link(self: Self) -> Self | None:
            """The property, reference to next node object.

            Args:
                self (Self): An object.

            Returns:
                Self | None: Return the reference to next node object in singly
                linked list if exists, None otherwise.
            """
            return self.__link

        @_link.setter
        def _link(self: Self, link: Self | None) -> None:
            """Mutate the property self._link before validating it.

            Args:
                self (Self): An object
                link (Self | None): Mutate property with this.

            Raises:
                TypeError: If link is not valid. In order link to be valid it
                need to be either LinkedStack._Node or None type.
            """
            if not self._valid_link(link):
                cls_name = self.__class__
                link_cls_name = link.__class__
                raise TypeError(
                    f"inappropriate type for the '_link': expecting either \
                    '{cls_name}' or '{None}' but got '{link_cls_name}'"
                )
            self.__link = link

        def __str__(self) -> str:
            """Implements str(self).

            Returns:
                str: Return the string representation of an object
            """
            cls_name = self.__class__.__name__
            return f"<{cls_name} contains {self._val}>"

    def __init__(self: Self) -> None:
        """Create an empty stack.

        Args:
            self (Self): An object.
        """
        self._head: LinkedStack._Node | None = None  # Reference to head node.
        self._size: int = 0  # Number of stack items.

    def __len__(self: Self) -> int:
        """Return the length the stack. Takes O(1) since explicitly maintaining
        size object which increment and decreament according to push and pop
        operation.

        Args:
            self (Self): An object.

        Returns:
            int: Number of items stored inside stack.
        """
        return self._size

    def is_empty(self: Self) -> bool:
        """Return True when stack is empty, False otherwise.

        Args:
            self (Self): An object.

        Returns:
            bool: Return True when stack is empty, False otherwise.
        """
        return len(self) == 0

    def push(self: Self, item: Any) -> None:
        """Add an item to the top of stack. Takes O(1) as inserting an item at
        the beginning of the singly linked list.

        Args:
            self (Self): An object.
            item (Any): An item that need to be added.
        """
        self._head = self._Node(item, self._head)
        self._size += 1

    def pop(self: Self) -> Any:
        """Remove and return the item from top of the stack (i.e. LIFO). Takes
        O(1) as removing an item at the beginning of the singly linked list.

        Args:
            self (Self): An object.

        Raises:
            Exception: Tring to remove an item from empty stack.

        Returns:
            Any: Return top of the stack.
        """
        if self._head is None:  # Or self.is_empty()
            raise Exception(f"cannot remove an item from an empty stack")
        value = self._head._val
        self._head = self._head._link
        self._size -= 1
        return value

    def top(self: Self) -> Any:
        """Return (but do not remove) the item at the top of the stack. Takes
        O(1) since no need to traverse the singly linked list as top of the
        stack present at the beginning.

        Args:
            self (Self): An object.

        Raises:
            Exception: Trying to return an item from empty stack.

        Returns:
            Any: The most recent item inserted into the stack.
        """
        if self._head is None:  # Or self.is_empty()
            raise Exception(f"cannot return an item from an empty stack")
        return self._head._val
