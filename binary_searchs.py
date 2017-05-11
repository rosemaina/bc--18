class BinarySearch(list):


    def __init__(self, a, b, *args):



        #list initialization

        list.__init__(self, *args)

        self.last = a

        self.step = b


        end = self.last + self.step


        for i in range(self.step, end, self.step):

            self.append(i)


        self.length = len(self)


    # executes binary search algorithm

    def search(self, element, bottom=0, top=None, count=0):


         # initialize the first and last indices

        first = 0

        last = len(self) - 1

        value_index = 0

        found = False


        """checks positon of a value in the array or list"""

        if not top:

            top = self.length - 1



        # checks if the value is the first

        elif element == self[top]:

            return {'index': top, 'count': count}

    # checks if the value is the last

        if element == self[bottom]:

            return {'index': bottom, 'count': count}

        #checks if the value is in the middle of the list or array

        mid = (bottom + top) // 2

        if element == self[mid]:

            return {'index': mid, 'count': count}


        
        # binary search algorithm using a while loop

        while first <= last and not found:

            mid = (first + last) // 2

            if self[mid] == element:

                found = True

                value_index = mid

                return {'count': count, 'index': value_index}

            else:



                if self[mid] < element:

                    first = mid + 1

                elif self[mid] > element:

                    last = mid -1

        count += 1

        if not found:

            return {'count': count, 'index': -1}


x = BinarySearch(78, 2)

print (x.search(78))