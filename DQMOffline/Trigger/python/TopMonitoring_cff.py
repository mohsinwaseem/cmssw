import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.TopMonitor_cfi import hltTOPmonitoring

dummy = hltTOPmonitoring.clone()
dummy.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/dummy/')
dummy.nmuons = cms.uint32(0)
dummy.nelectrons = cms.uint32(1)
dummy.njets = cms.uint32(2)
dummy.eleSelection = cms.string('pt>15 & abs(eta)<2.4')
dummy.jetSelection = cms.string('pt>20 & abs(eta)<2.4')
dummy.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned')
dummy.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned')

test = hltTOPmonitoring.clone()
test.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/test/')
test.nmuons = cms.uint32(0)
test.nelectrons = cms.uint32(1)
test.njets = cms.uint32(2)
test.eleSelection = cms.string('pt>15 & abs(eta)<2.4')
test.jetSelection = cms.string('pt>20 & abs(eta)<2.4')
test.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned')
test.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_v*')

test2 = hltTOPmonitoring.clone()
test2.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/test2/')
test2.nmuons = cms.uint32(0)
test2.nelectrons = cms.uint32(1)
test2.njets = cms.uint32(2)
test2.eleSelection = cms.string('pt>15 & abs(eta)<2.4')
test2.jetSelection = cms.string('pt>20 & abs(eta)<2.4')
test2.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned')

#ATHER
topSingleMuonHLTValidation = hltTOPmonitoring.clone()
topSingleMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/SingleLepton/SingleMuon/')
topSingleMuonHLTValidation.nmuons = cms.uint32(1)
topSingleMuonHLTValidation.nelectrons = cms.uint32(0)
topSingleMuonHLTValidation.njets = cms.uint32(4)
topSingleMuonHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topSingleMuonHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')
topSingleMuonHLTValidation.jetSelection = cms.string('pt>20 & abs(eta)<2.5')
topSingleMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu20_v*', 'HLT_TkMu20_v*' , 'HLT_Mu27_v*', 'HLT_TkMu27_v*', 'HLT_TkMu50_v*', 'HLT_Mu50_v*', 'HLT_IsoMu24_eta2p1_v*', 'HLT_IsoMu24_v*', 'HLT_IsoMu27_v*', 'HLT_IsoMu20_v*', 'HLT_IsoTkMu24_eta2p1_v*', 'HLT_IsoTkMu24_v*', 'HLT_IsoTkMu27_v*', 'HLT_IsoTkMu20_v*'])
topSingleMuonHLTValidation.useReferenceTrigger = cms.bool(False)

#topSingleElectronHLTValidation = hltTOPmonitoring.clone()
#topSingleElectronHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/SingleLepton/SingleElectron/')
#topSingleElectronHLTValidation.nmuons = cms.uint32(0)
#topSingleElectronHLTValidation.nelectrons = cms.uint32(1)
#topSingleElectronHLTValidation.njets = cms.uint32(4)
#topSingleElectronHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5')            
#topSingleElectronHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1')   
#topSingleElectronHLTValidation.jetSelection = cms.string('pt>20 & abs(eta)<2.5')
#topSingleElectronHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring('')
#topSingleElectronHLTValidation.useReferenceTrigger = cms.bool(False)

topDiElectronHLTValidation = hltTOPmonitoring.clone()
topDiElectronHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/DiElectron/')
topDiElectronHLTValidation.nmuons = cms.uint32(0)
topDiElectronHLTValidation.nelectrons = cms.uint32(2)
topDiElectronHLTValidation.njets = cms.uint32(2)
topDiElectronHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5  & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topDiElectronHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')   
topDiElectronHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topDiElectronHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Ele12_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*'])
topDiElectronHLTValidation.useReferenceTrigger = cms.bool(False)


topDiMuonHLTValidation = hltTOPmonitoring.clone()
topDiMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/DiMuon/')
topDiMuonHLTValidation.nmuons = cms.uint32(2)
topDiMuonHLTValidation.nelectrons = cms.uint32(0)
topDiMuonHLTValidation.njets = cms.uint32(2)
topDiMuonHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5  & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')              
topDiMuonHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')  
topDiMuonHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topDiMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*','HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*'])
topDiMuonHLTValidation.useReferenceTrigger = cms.bool(False)


topElecMuonHLTValidation = hltTOPmonitoring.clone()
topElecMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/ElecMuon/')
topElecMuonHLTValidation.nmuons = cms.uint32(1)
topElecMuonHLTValidation.nelectrons = cms.uint32(1)
topElecMuonHLTValidation.njets = cms.uint32(2)
topElecMuonHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topElecMuonHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')           
topElecMuonHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topElecMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*','HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'])
topElecMuonHLTValidation.useReferenceTrigger = cms.bool(False)


singleTopSingleMuonHLTValidation = hltTOPmonitoring.clone()
singleTopSingleMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/SingleTop/SingleMuon/')
singleTopSingleMuonHLTValidation.nmuons = cms.uint32(1)
singleTopSingleMuonHLTValidation.nelectrons = cms.uint32(0)
singleTopSingleMuonHLTValidation.njets = cms.uint32(2)
singleTopSingleMuonHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')   
singleTopSingleMuonHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')
singleTopSingleMuonHLTValidation.jetSelection = cms.string('pt>40 & abs(eta)<5.0')
singleTopSingleMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu20_v*', 'HLT_TkMu20_v*' , 'HLT_Mu27_v*', 'HLT_TkMu27_v*', 'HLT_TkMu50_v*', 'HLT_Mu50_v*', 'HLT_IsoMu24_eta2p1_v*', 'HLT_IsoMu24_v*', 'HLT_IsoMu27_v*', 'HLT_IsoMu20_v*', 'HLT_IsoTkMu24_eta2p1_v*', 'HLT_IsoTkMu24_v*', 'HLT_IsoTkMu27_v*', 'HLT_IsoTkMu20_v*'])
singleTopSingleMuonHLTValidation.useReferenceTrigger = cms.bool(False)

#singleTopSingleElectronHLTValidation = hltTOPmonitoring.clone()
#singleTopSingleElectronHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/SingleTop/SingleElectron/')
#singleTopSingleElectronHLTValidation.nmuons = cms.uint32(0)
#singleTopSingleElectronHLTValidation.nelectrons = cms.uint32(1)
#singleTopSingleElectronHLTValidation.njets = cms.uint32(2)
#singleTopSingleElectronHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5')     
#singleTopSingleElectronHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1')       
#singleTopSingleElectronHLTValidation.jetSelection = cms.string('pt>40 & abs(eta)<5.0')
#singleTopSingleElectronHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring('')
#singleTopSingleElectronHLTValidation.useReferenceTrigger = cms.bool(False)


topMonitorHLT = cms.Sequence(
    dummy
    + test
    + test2
    + topSingleMuonHLTValidation
    + topSingleElectronHLTValidation
    + topDiElectronHLTValidation
    + topDiMuonHLTValidation
    + topElecMuonHLTValidation
    + singleTopSingleMuonHLTValidation
    + singleTopSingleElectronHLTValidation
)
