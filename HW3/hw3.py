import csv

class HWReader:
    """class HWReader to get SAPS-1 score and average
        with giving conditions

        Typical usage example:

        csv_data = HWReader("data.csv")
    """
    def __init__(self, filename):
        """initializetion for HWReader class

        Args:
            filename: input string of a csv file name.

        Returns:
            loaded csv file
        """
        self.input_dict = {}
        self.filename = filename

        #read input csv
        with open(self.filename, mode = 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.next_item = next(csv_reader)
            for row in csv_reader:
                for index, column in enumerate(self.next_item):
                    self.input_dict.setdefault(column, []).append(row[index])

    def get_saps(self, record_id):
        """gets the SAPS score for input record

        Typical usage example:

        print(csv_data.get_saps("132582"))

        Args:
            record_id: the RecordID to allocate the correspondin info

        Returns:
            SAPS_score: float type, calculated score
        """
        record_id_str = str(record_id)
        #allocate to corresponding columne of RecordID and get index values
        record_id_index = self.input_dict['RecordID'].index(record_id_str)
        #get SAPS score with the help of record_id_index
        SAPS_score = self.input_dict['SAPS-I'][record_id_index]
        return float(SAPS_score)

    def calc_avg(self, columne_name, filter, logic, threshold):
        """calculates the average of input columne with 
        different conditions.

        Typical usage example:

        print(csv_data.calc_avg("Length_of_stay", filter="SOFA", logic="lt", threshold="15"))

        Args:
            columne_name: input name of the columne within the csv file.
            filter: user chosen input for the filter
            logic: user chosen logic, such as less than, greater than, etc.
            threshhold: user chosen number to be compared with the help of logic

        Returns:
            avg: float type, the calculated average.
        """
        input_filter = enumerate(self.input_dict[filter])

        #conditions for all 4 possible inputs for logic, 
        #less than, greater than, less than equal, and greater than equal
        if logic == 'lt':
            filter_index = [
                index for index, value in input_filter 
                if float(value) < float(threshold)
            ]

        elif logic == 'gt':
            filter_index = [
                index for index, value in input_filter 
                if float(value) > float(threshold)
            ]

        elif logic == 'lte':
            filter_index = [
                index for index, value in input_filter 
                if float(value) <= float(threshold)
            ]

        elif logic == 'gte':
            filter_index = [
                index for index, value in input_filter 
                if float(value) >= float(threshold)
            ]

        #if user input isn't the 4 above, print out error message
        else:
            error_message = 'please give a correct input logic, such as lt, gt, lte, or gte'
            return error_message
            
        result = [float(self.input_dict[columne_name][i]) for i in filter_index]
        
        #calculate average result
        sum_num = 0
        for t in result:
            sum_num = sum_num + t
            avg = sum_num / len(result)

        return avg
        