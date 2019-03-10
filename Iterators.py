# We can create our own iterable objects, let's see how is that


# first of all let's create a class



# class tvChannels():

#     def __init__(self, channelName):

#         self.channelName = channelName

# channels = tvChannels(["Channel A", "Channel B", "Channel C"])

#Now let's try to use for loop on channels:

# for names in channels:
#     print(channels)

# As you can see we got an error: "TypeError: 'tvChannels' object is not iterable"

#Now let's make this object to Iterable object!
# For this we need to define __iter__ and __next__ functions to our class.

class tvChannels():

    def __init__(self, channelName):

        self.channelName = channelName
        self.currentChannel = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.currentChannel += 1
        if self.currentChannel < len(self.channelName):
            return "Now you're on:", self.channelName[self.currentChannel]
        else:
            self.currentChannel = -1
            raise StopIteration

            

channels = tvChannels(["Channel A", "Channel B", "Channel C"])
ITchannels = iter(channels)
print(next(ITchannels)) #First index:   Channel A
print(next(ITchannels)) #Second Index:  Channel B
print(next(ITchannels)) #Third Index:   Channel C
print(next(ITchannels)) #Third Index:   Channel C

ITchannelsx = iter(channels)

for f in ITchannelsx:
    print("sds")
    print(f)