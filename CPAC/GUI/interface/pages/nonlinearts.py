import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator
import pkg_resources as p


class NonLinearTimeSeriesAnalysis(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        #self.LoadPage(p.resource_filename('CPAC', 'GUI/resources/html/nuisance.html'))
            
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/nuisance.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/nuisance.html')
#            else:
#                self.LoadFile('html/nuisance.html')
#        except:
#            self.LoadFile('html/nuisance.html')
            
            
    def get_counter(self):
        return self.counter

        
class Preanalysis(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        
        self.counter = counter

        
        self.page = GenericClass(self, "Preanalysis Measures Calculation Options")
        
        self.page.add(label="Run Timeseries Preanalysis Measures", 
                 control=control.CHOICE_BOX, 
                 name='runPre', 
                 type=dtype.LSTR, 
                 comment="Run Timseries Preanalysis Measures", 
                 values=["Off","On"],
                 wkf_switch = True)
                 
        self.page.add(label="Voxelwise / ROI extraction", 
                 control=control.CHOICE_BOX, 
                 name='voxel_roi', 
                 type=dtype.LSTR, 
                 comment="Run Information Theory Measures voxelwise or after ROI timeseries extraction", 
                 values=["Voxelwise","ROI"],
                 wkf_switch = True)         
        
        self.page.add(label="fMRI image", 
                     control=control.COMBO_BOX, 
                     name='input_image', 
                     type=dtype.STR, 
                     comment="fMRI image for calculation")
       
        self.page.add(label="Parcellation Mask", 
                     control=control.COMBO_BOX, 
                     name='input_mask', 
                     type=dtype.STR, 
                     comment="Parcellation Mask if you want to calculate")


        self.page.add(label = "Measures:",
                      #control = control.CHECKLISTBOX_COMBO,
                      control = control.LISTBOX_COMBO,
                      name = "Measures",
                      type = dtype.LDICT,
                      values = ['Correlation', 'Partial Correlation','Phase Syncrhonization Index','Phase Locking Value'],
                      comment = "Select which preanalysis measures to apply:\n"\
                                "corr = Entropy\n"\
                                 "pcorr = Conditional Entropy\n"\
                                 "PSI = Phase Syncrhonization Index\n"\
                                 "PLV = Phase Locking Value\n",
                     size = (300,120),
                     combo_type =1)
     
        self.page.add(label="Output Options ",
                      control=control.CHECKLIST_BOX,
                      name="measure_options",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY','NIFTI'],
                      comment="By default, results are written as NIFTI files. Additional output formats are as a .csv spreadsheet or a Numpy array.")


        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
            
class IT(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        
        self.counter = counter

        
        self.page = GenericClass(self, "Information Theory Calculation Options")
        
        self.page.add(label="Run Information Theory Measures", 
                 control=control.CHOICE_BOX, 
                 name='runIT', 
                 type=dtype.LSTR, 
                 comment="Run Information Theory Measures", 
                 values=["Off","On"],
                 wkf_switch = True)
                 
        self.page.add(label="Voxelwise / ROI extraction", 
                 control=control.CHOICE_BOX, 
                 name='voxel_roi', 
                 type=dtype.LSTR, 
                 comment="Run Information Theory Measures voxelwise or after ROI timeseries extraction", 
                 values=["Voxelwise","ROI"],
                 wkf_switch = True)         
        
        self.page.add(label="fMRI image", 
                     control=control.COMBO_BOX, 
                     name='input_image', 
                     type=dtype.STR, 
                     comment="fMRI image for calculation")
       
        self.page.add(label="Parcellation Mask", 
                     control=control.COMBO_BOX, 
                     name='input_mask', 
                     type=dtype.STR, 
                     comment="Parcellation Mask if you want to calculate")


        self.page.add(label = "Measures:",
                      #control = control.CHECKLISTBOX_COMBO,
                      control = control.LISTBOX_COMBO,
                      name = "Measures",
                      type = dtype.LDICT,
                      values = ['Entropy', 'Conditional Entropy','Mutual Information','Transfer Entropy','Entropy Correlation Coefficient'],
                      comment = "Select which IT measures to apply:\n"\
                                "ent = Entropy\n"\
                                 "condent = Conditional Entropy\n"\
                                 "mi = Mutual Information\n"\
                                 "te = Transfer Entropy\n"\
                                 "ecc = Entropy Correlation Coefficient\n",
                     size = (300,120),
                     combo_type =1)
     
        self.page.add(label="Output Options ",
                      control=control.CHECKLIST_BOX,
                      name="measure_options",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY','NIFTI'],
                      comment="By default, results are written as NIFTI files. Additional output formats are as a .csv spreadsheet or a Numpy array.")


        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
class SFD(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Scale Free Dynamics")
        
        self.page.add(label="Run SFD measures", 
                 control=control.CHOICE_BOX, 
                 name='runCausality', 
                 type=dtype.LSTR, 
                 comment="Scale free dynamics", 
                 values=["Off","On"],
                 wkf_switch = True)
                 
        self.page.add(label="Voxelwise / ROI extraction", 
                 control=control.CHOICE_BOX, 
                 name='voxel_roi', 
                 type=dtype.LSTR, 
                 comment="Run Information Theory Measures voxelwise or after ROI timeseries extraction", 
                 values=["Voxelwise","ROI"],
                 wkf_switch = True)         
        
        self.page.add(label="fMRI image", 
                     control=control.COMBO_BOX, 
                     name='input_image', 
                     type=dtype.STR, 
                     comment="fMRI image for calculation")
       
        self.page.add(label="Parcellation Mask", 
                     control=control.COMBO_BOX, 
                     name='input_mask', 
                     type=dtype.STR, 
                     comment="Parcellation Mask if you want to calculate")         
                 
        self.page.add(label = "Measures:",
                      #control = control.CHECKLISTBOX_COMBO,
                      control = control.LISTBOX_COMBO,
                      name = "Measures",
                      type = dtype.LDICT,
                      values = ['DFA', 'Fractality','Avalanches'],
                      comment = "Select which IT measures to apply:\n"\
                                "dfa = Detrended Fluctuation Analysis\n"\
                                 "fractal = Fractality\n"\
                                 "aval = Avalanches\n",
                     size = (300,120),
                     combo_type =1)         
        
        self.page.add(label="Output Options ",
                      control=control.CHECKLIST_BOX,
                      name="measure_options",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY','NIFTI'],
                      comment="By default, results are written as NIFTI files. Additional output formats are as a .csv spreadsheet or a Numpy array.")


        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
            